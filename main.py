if __name__ == '__main__':
    from Forward_func import forward
    import json
    forward(*list(json.load(open('/home/mekkoandy/development/nft_generators/gif/params.json', 'r')).values()))
