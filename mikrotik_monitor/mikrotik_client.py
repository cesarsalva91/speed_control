from librouteros import connect

def get_nat_stats(router):
    try:
        api = connect(username=router.user, password=router.password, host=router.ip, port=router.port)
        rules = api.path("ip", "firewall", "nat")
        return [{
            'id': rule.get('.id'),
            'bytes': rule.get('bytes'),
            'packets': rule.get('packets'),
            'comment': rule.get('comment')
        } for rule in rules]
    except Exception as e:
        print(f"[ERROR] Conexión fallida a {router.ip}: {e}")
        return []
