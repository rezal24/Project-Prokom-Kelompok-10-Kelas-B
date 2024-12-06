def hitung_biaya_dasar(jenis_dasar):
    harga_dasar = {
        "kecil" : 25000,
        "sedang" : 35000,
        "besar" : 45000
    }
    return harga_dasar.get(jenis_dasar, 0)

def hitung_biaya_saus(jenis_saus):
    harga_saus = {
        "tomat" : 10000,
        "pesto" : 10000,
        "bbq" : 10000
    }
    return harga_saus.get(jenis_saus, 0)

def hitung_biaya_keju(jenis_keju):
    harga_keju = {
        "cheddar": 10000,
        "mozzarella": 12000,
        "parmesan": 15000
    }
    return harga_keju.get(jenis_keju, 0)

def hitung_biaya_topping(nama_topping):
    harga_topping = {
        "bawang": 10000,
        "jagung": 10000,
        "olive": 10000,
        "nanas": 10000,
        
        "jamur": 12000,
        "paprika": 12000,
        "sosis ayam": 12000,
        "parsley": 12000,
        "tuna": 12000,
        "jalapeno": 12000,
        
        "pepperoni": 15000,
        "sosis sapi": 15000,
        "meatball": 15000,
        "beef burger": 15000,
        "macaroni": 15000
    }
    return harga_topping.get(nama_topping.lower(), 0)