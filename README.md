<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Dizin Tarama Programı</title>
</head>
<body>
    <h1>Web Dizin Tarama Programı</h1>
    <p>Bu Python programı, verilen bir başlangıç URL'sinden başlayarak belirtilen derinlikte web sayfalarını taramak için kullanılır. Program, belirli özel kelimeleri arar, belirli bir derinliğe kadar gezinir ve bulunan bağlantıları kaydedebilir.</p>
    <h2>Özellikler</h2>
    <ul>
        <li>Belirtilen URL'den başlayarak derinliğe kadar web sayfalarını tarar.</li>
        <li>Görsel bağlantıları da taramak isteyenler için bir seçenek sunar.</li>
        <li>Arama sonuçlarını belirtilen özel kelimelerle filtreler.</li>
        <li>Tüm bağlantıları kaydetme seçeneği sunar.</li>
        <li>Bağlantılar arasında özel kelime bulunanları ve resim bağlantılarını belirtir.</li>
    </ul>
    <h2>Kullanım</h2>
    <ol>
        <li>Başlangıç URL'sini girin.</li>
        <li>Tarama derinliğini belirtin.</li>
        <li>Görsel bağlantıları da taramak istiyorsanız "E" seçeneğini seçin.</li>
        <li>Özel kelimeleri virgülle ayırarak belirtin.</li>
        <li>Tüm bağlantıları kaydetmek istiyorsanız "E" seçeneğini seçin.</li>
    </ol>
    <h2>Nasıl Çalıştırılır</h2>
    <p>Python 3.6 veya üstü gereklidir. Programı çalıştırmak için aşağıdaki komutu kullanabilirsiniz:</p>
    <pre><code>python web_dizin_tarama.py</code></pre>
    <h2>Ekran Görüntüsü</h2>
    <img src="screenshot.png" alt="Web Dizin Tarama Programı Ekran Görüntüsü">
    <h2>Notlar</h2>
    <ul>
        <li>Programın çalışması için <code>requests</code>, <code>beautifulsoup4</code> ve <code>colorama</code> kütüphanelerinin yüklü olması gerekmektedir.</li>
        <li>Programın çalışması birtakım hatalara neden olabilir, bu nedenle dikkatli kullanılmalıdır.</li>
        <li>Programın kaynak kodunu dilediğiniz gibi değiştirebilir ve geliştirebilirsiniz.</li>
    </ul>
</body>
</html>
