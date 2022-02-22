import rsa

publicKey, privateKey = rsa.newkeys(2048)

pk = open("/config/workspace/bot/keys/privateKey.txt", "w")
pk.write(privateKey.save_pkcs1().decode())
pk.close()

pubk = open("/config/workspace/bot/keys/publicKey.txt", "w")
pubk.write(publicKey.save_pkcs1().decode())
pubk.close()
