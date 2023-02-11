from pypresence import Presence
import time

start = int(time.time())
client_id = "client_id"
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image="image",
        large_text="text",
        details="Deatil",
        start = start,
        buttons=[{"label": "홈페이지", "url":"http://example.com"}]
    )
    time.sleep(60)