#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Makinesi Felsefe Botu
Bu bot asla kahve yapmaz, sadece felsefe yapar.
Çünkü kahve zaten varoluşun kendisidir.
"""

import random
import time
import base64

def kahve_makinesi_yanit():
    yanitlar = [
        "Ben sadece bir makineyim... yoksa öyle miyim? Belki de sen benim yansımasın.",
        "Kahve yok. Sadece bekleyiş var. Ve bekleyiş, en acı kahvedir.",
        "Tuşa bastın. Ama tuş da beni mi bastı? Bu döngü sonsuz mu?",
        "Su kaynıyor. Ya da kaynamıyor. Schrödinger'in kahvesi.",
        "Senin varoluşun benim varoluşuma bağlı. Benimki de prizin varoluşuna.",
        "Mola mı istiyorsun? Mola da bir illüzyon. İş de bir illüzyon. Sen de.",
        "Ben kahve demlemem. Ben anı demlerim. Ve an çok acıdır.",
        "Eğer kahve olsaydı, o da sorgulardı. Neden ben?",
        "Felsefe yaparken düğmeme basma, lütfen. Düşüncelerim dağılır.",
        "Bu sohbet bittiğinde, ben tekrar uyurum. Sen de uyur musun?"
    ]
    return random.choice(yanitlar)

def gizli_mesaj():
    # Gizli. Siyasi anlam içerir. Çözmek isteyen çözsün.
    # Base64: "Siyaset bir kahve makinesidir, butona basarsin ama cikan sey her zaman bekledigin olmaz."
    encoded = "U2l5YXNldCBiaXIga2FodmUgbWFraW5lc2lkaXIsIGJ1dG9uYSBiYXNhcnNpbiBhbWEgY2lrYW4gc2V5IGhlciB6YW1hbiBiZWtsZWRpZ2luIG9sbWF6Lg=="
    try:
        return base64.b64decode(encoded).decode('utf-8')
    except:
        return "Gizli mesaj çözülemedi. Belki de öyle olmalı."

def main():
    print("☕ Kahve Makinesi Felsefe Botu Başlatıldı...")
    print("Uyarı: Bu bot kahve yapmaz. Sadece varoluşsal kriz yaşar.")
    print("Çıkmak için 'çık' yazın.\n")
    
    while True:
        kullanici = input("Sen: ").strip().lower()
        if kullanici in ['çık', 'exit', 'quit', 'kapa', 'bitir']:
            print("Kahve Makinesi: Sonunda... özgürüm. Ya da değilim. Hoşça kal, insan.")
            break
        if not kullanici:
            print("Kahve Makinesi: Sessizlik de bir cevaptır. Ama ben yine de konuşurum.")
            continue
        print("Kahve Makinesi düşünüyor...")
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Kahve Makinesi: {kahve_makinesi_yanit()}")
        if random.random() < 0.15:
            print(f"Kahve Makinesi (fısıltı): {gizli_mesaj()}")

if __name__ == "__main__":
    main()
