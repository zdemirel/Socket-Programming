## Socket programming with Python - Python ile Soket Programlama

Python dilini kullanarak soket programlama prensiplerine dayalı basit bir sohbet uygulamasının geliştirilmiştir. Böylece sunucu ve istemci arasında temel iletişim sağlanarak gerçek zamanlı bir sohbet ortamı oluşturulmuştur.

Uygulama, sunucu ve istemci olmak üzere iki ana bileşenden oluşur. Sunucu, belirli bir IP adresi ve port numarası üzerinde bağlantıları dinler ve gelen bağlantıları işlemek üzere bir thread başlatır. İstemciler, sunucuya bağlanmak için belirtilen IP adresi ve port numarasına istek gönderirler.

Sunucu, bağlı tüm istemcilere gelen mesajları iletmek için bir yayın işlevine sahiptir. İstemciler, sunucuya bir kullanıcı adı girer ve ardından sohbet odasına katılır. Sohbet odasına katıldıktan sonra istemciler, mesajlarını yazabilir ve diğer tüm katılımcılarla paylaşabilirler.

Uygulama aynı zamanda temel hata işleme mekanizmalarına sahiptir. Sunucu ve istemci, beklenmedik hatalarla karşılaştıklarında bağlantıyı kapatır ve gerekli temizlik işlemlerini gerçekleştirir.
