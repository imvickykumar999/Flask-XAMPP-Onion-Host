# Host-Onion

`Steps to Host on Tor`

    Tutorial: 
        https://youtu.be/Yj_ta_xdKf4

    XAMPP Control Panel (click start on apache):
        Module: Apache
        Action: Start

    torrc (paste 3 lines): 
    C:\Users\Vicky\Tor Browser\Browser\TorBrowser\Data\Tor\

        #HiddenService
        HiddenServiceDir C:\Users\Vicky\Tor Browser\domain name
        HiddenServicePort 80 127.0.0.1

    index.html (add ftml files here): 
        C:\xampp\htdocs

    localhost (test locally):
        http://127.0.0.1/
        
    Open Tor Browser (files will generate):
        C:\Users\Vicky\Tor Browser\domain name

    hostname (Tor link generated):
        bkiwy4lhsoyvbxmnhee6eyv7mjz5v4ptzoyp7iejqicqh73rhf7lvead.onion

    access.log (see realtime logs): 
        C:\xampp\apache\logs

    (optional, to down site)
        XAMPP Control Panel (click stop on apache):
            Module: Apache
            Action: Stop
