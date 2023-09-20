># Host Onion Websites
>
>![image](https://github.com/imvickykumar999/Host-Onion/assets/50515418/5ccf936b-9c7c-4c50-9c25-2e6cc32c8667)

<br>

## `Steps to Host on Tor`

    Fun Fact: 
        onion sites are hosted locally on your device (Laptop, Raspberry Pi, etc.)

<br>

    Tutorial: 
        https://youtu.be/Yj_ta_xdKf4

    Also, Host on Raspberry Pi
        https://youtu.be/bllS9tkCkaM

    XAMPP Control Panel (click start on apache):
        Module: Apache
        Action: Start

    torrc (paste 3 lines): 
    C:\Users\Vicky\Tor Browser\Browser\TorBrowser\Data\Tor\

        #HiddenService
        HiddenServiceDir C:\Users\Vicky\Tor Browser\domain name
        HiddenServicePort 80 127.0.0.1

    index.html (add html files here): 
        C:\xampp\htdocs

    localhost (test locally):
        http://127.0.0.1/

        or,
        http://localhost/index.html
        
    Open Tor Browser 
        Start Tor Browser (.shortcut)
            C:\Users\Vicky\Tor Browser

        (files will generate at):
            C:\Users\Vicky\Tor Browser\domain name

    hostname (Tor link generated):
        bkiwy4lhsoyvbxmnhee6eyv7mjz5v4ptzoyp7iejqicqh73rhf7lvead.onion

    access.log (see realtime logs): 
        C:\xampp\apache\logs

    (optional, to down the site)
        Close/Disconnect Tor Browser

        and,
        XAMPP Control Panel (click stop on apache):
            Module: Apache
            Action: Stop
