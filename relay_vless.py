# relay_vless.py - نسخه نهایی پایدار (بدون خطا)

import asyncio
import socket
import logging
from datetime import datetime

logger = logging.getLogger("RVG-Gateway")
RELAY_BUF = 64 * 1024

# ========== تنظیمات Xray ==========
XRAY_HOST = "127.0.0.1"
XRAY_PORT = 443  # پورت پیش‌فرض Xray

async def relay_ws_to_tcp(websocket, sock, uuid):
    """Relay از WebSocket به TCP"""
    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_bytes(), timeout=30.0)
                if not data:
                    break
                sock.sendall(data)
            except asyncio.TimeoutError:
                continue
            except:
                break
    except:
        pass
    finally:
        try:
            sock.close()
        except:
            pass

async def relay_tcp_to_ws(websocket, sock, uuid):
    """Relay از TCP به WebSocket"""
    loop = asyncio.get_event_loop()
    try:
        while True:
            try:
                data = await asyncio.wait_for(loop.sock_recv(sock, RELAY_BUF), timeout=30.0)
                if not data:
                    break
                await websocket.send_bytes(data)
            except asyncio.TimeoutError:
                continue
            except:
                break
    except:
        pass
    finally:
        try:
            sock.close()
        except:
            pass

async def parse_vless_header(chunk: bytes):
    """پارسر ساده VLESS header"""
    if len(chunk) < 24:
        raise ValueError("chunk too small")
    pos = 1
    pos += 16
    addon_len = chunk[pos]
    pos += 1 + addon_len
    command = chunk[pos]
    pos += 1
    port = int.from_bytes(chunk[pos:pos+2], "big")
    pos += 2
    addr_type = chunk[pos]
    pos += 1
    if addr_type == 1:
        address = ".".join(str(b) for b in chunk[pos:pos+4])
        pos += 4
    elif addr_type == 2:
        dlen = chunk[pos]
        pos += 1
        address = chunk[pos:pos+dlen].decode("utf-8", errors="ignore")
        pos += dlen
    elif addr_type == 3:
        ab = chunk[pos:pos+16]
        pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return command, address, port, chunk[pos:]

async def check_and_use(uuid: str, n: int) -> bool:
    """بررسی اعتبار و افزایش مصرف"""
    try:
        from main import LINKS, LINKS_LOCK, is_link_allowed, stats, hourly_traffic, now_ir
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
            if link is None:
                return False
            if not is_link_allowed(link):
                return False
            link["used_bytes"] = link.get("used_bytes", 0) + n
            stats["total_bytes"] = stats.get("total_bytes", 0) + n
            hourly_traffic[now_ir().strftime("%H:00")] = hourly_traffic.get(now_ir().strftime("%H:00"), 0) + n
        return True
    except Exception as e:
        logger.error(f"check_and_use error: {e}")
        return False

async def websocket_tunnel(websocket, uuid: str):
    """WebSocket Tunnel اصلی"""
    from main import connections, LINKS, LINKS_LOCK, log_activity, is_link_allowed
    
    client_addr = websocket.client.host if websocket.client else "unknown"
    logger.info(f"🔗 New connection: {uuid} from {client_addr}")
    
    # بررسی اعتبار کاربر
    try:
        async with LINKS_LOCK:
            link = LINKS.get(uuid)
            if not link:
                await websocket.close(code=1008, reason="User not found")
                logger.warning(f"❌ User not found: {uuid}")
                return
            if not is_link_allowed(link):
                await websocket.close(code=1008, reason="User inactive or expired")
                logger.warning(f"❌ User inactive/expired: {uuid}")
                return
            logger.info(f"✅ User validated: {uuid} - {link.get('label', 'Unknown')}")
    except Exception as e:
        logger.error(f"❌ Auth error: {e}")
        try:
            await websocket.close(code=1011, reason="Internal error")
        except:
            pass
        return
    
    sock = None
    try:
        # اتصال به Xray
        logger.info(f"🔗 Connecting to Xray: {XRAY_HOST}:{XRAY_PORT}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((XRAY_HOST, XRAY_PORT))
        sock.settimeout(None)
        logger.info(f"✅ Connected to Xray: {XRAY_HOST}:{XRAY_PORT}")
        
        # ذخیره اتصال
        connections[uuid] = {
            "ip": client_addr,
            "uuid": uuid,
            "connected_at": datetime.now().isoformat(),
            "transport": "vless-ws",
            "bytes": 0,
        }
        
        log_activity("connection", f"اتصال جدید از {client_addr} (کانفیگ {link.get('label','?')})", "ok")
        
        # شروع Relay
        await asyncio.gather(
            relay_ws_to_tcp(websocket, sock, uuid),
            relay_tcp_to_ws(websocket, sock, uuid)
        )
        
    except ConnectionRefusedError:
        logger.error(f"🚫 Xray is NOT running on {XRAY_HOST}:{XRAY_PORT}")
        logger.error("💡 Please install and start Xray first!")
        logger.error("💡 Run: bash -c \"$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)\" @ install")
        try:
            await websocket.close(code=1011, reason="Xray not running")
        except:
            pass
        
    except socket.timeout:
        logger.error(f"⏱️ Connection timeout to Xray: {XRAY_HOST}:{XRAY_PORT}")
        try:
            await websocket.close(code=1011, reason="Connection timeout")
        except:
            pass
        
    except Exception as e:
        logger.error(f"❌ WS error: {e}")
        try:
            await websocket.close(code=1011, reason=f"Error: {str(e)[:50]}")
        except:
            pass
        
    finally:
        # پاکسازی
        connections.pop(uuid, None)
        if sock:
            try:
                sock.close()
            except:
                pass
        try:
            await websocket.close()
        except:
            pass
        log_activity("connection", f"اتصال {uuid} قطع شد", "info")
        logger.info(f"👋 Disconnected: {uuid}")
