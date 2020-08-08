m_start = 'Halo, selamat datang di anonymous chat bot! gunakan /start untuk memulai chat dan /stop untuk mengakhiri chat'

m_is_not_free_users = 'Maaf!! untuk saat ini, tidak ada pengguna aktif. ' \
                   'Kami akan menghubungimu ketika sudah ada pengguna aktif yang tersedia!'
m_is_connect = 'Anda sudah terhubung dengan pengguna lain!'

m_play_again = 'Ingin mengobrol dengan yang lainnya lagi?'

m_is_not_user_name = 'Untuk menggunakan bot ini, kamu harus memiliki username telegram. \n' \
                    'Kamu bisa mengaturnya di settings->username.'

m_good_bye = 'Bot: Selamat tinggal, senang bisa bertemu denganmu!'

m_disconnect_user = 'Lawan bicaramu telah mengakhiri percakapan' \
                    'Silahkan klik tombol dibawah ini untuk mulai percakapan baru'

m_failed = 'Bot: Terdapat kesalahan!'

m_like = 'Bot: Pilihan yang bagus!'

m_dislike_user = 'Bot: Obrolan sudah berakhir'

m_dislike_user_to = 'Bot: Lawan bicara tidak menyukaimu, maaf!'

m_send_some_messages = 'Bot: Kamu tidak dapat mereply percakapan mu sendiri!'

m_has_not_dialog = 'Kamu sedang tidak masuk ke obrolan'

dislike_str = '\U0001F44E Dislike'

like_str = '\U0001F44D Like'




def m_all_like(x):
    return 'Lawan bicaramu menyukaimu!\n' + 'Loginnya: ' + str(x) + \
           '\nSemoga beruntung!\nTerima kasih telah bersama kami!'
