># `Host Onion Websites`
>
>![image](https://github.com/imvickykumar999/XAMPP-Onion-Host/assets/50515418/c7cfdbba-b070-4993-bf9a-d3b3bfecd713)

<br>

## `Steps to Host on Tor`

    Fun Fact: 
        onion sites are hosted locally on your device (Laptop, Raspberry Pi, etc.)

<br>

    Tutorial (Server Host):
        Single Server:
            https://youtu.be/Yj_ta_xdKf4

        Multiple Server (optional):
            https://youtu.be/M4E7UgKiw34

    Also, Host on Raspberry Pi
        https://youtu.be/bllS9tkCkaM

    torrc (paste 3 lines): 
    C:\Users\Vicky\Tor Browser\Browser\TorBrowser\Data\Tor\

        HiddenServiceDir C:\Users\Vicky\Tor Browser\haystak
        HiddenServicePort 80 haystak.localhost

        # (optional)
        HiddenServiceDir C:\Users\Vicky\Tor Browser\hackers
        HiddenServicePort 80 hackers.localhost

    index.html (add html files here): 
        C:\xampp\htdocs

    Hosted Multiple .onion links (optional)
        https://stackoverflow.com/a/42810629/11493297

    httpd-vhosts.conf (optional)
        C:\xampp\apache\conf\extra

            ServerName hackers.localhost
            DocumentRoot "C:\xampp\htdocs\hackers"

    httpd-ssl.conf
        https://stackoverflow.com/a/71018094/11493297
            C:\xampp\apache\conf\extra

    hosts (optional)
    (to edit hosts file, Run Notepad as Administrator)
        C:\Windows\System32\drivers\etc

            127.0.0.1  haystak.localhost
            127.0.0.1  hackers.localhost

    localhost (test locally):
        (On normal browser)

            localhost.index.html
            or,
            http://127.0.0.1/

            (optional)
            http://hackers.localhost/
            http://haystak.localhost/
        
    XAMPP Control Panel (click start on apache):
        Module: Apache
        Action: Start

    Open Tor Browser 
        Start Tor Browser (.shortcut)
            C:\Users\Vicky\Tor Browser

        (files will generate at):
            C:\Users\Vicky\Tor Browser\domain name

    hostname (Tor link generated):
        i5hfkdpxlqjbojuiqt242h5vtgvic7jyzkfkj5ttdcatwycudprl74qd.onion

    access.log (optional, see realtime logs): 
        C:\xampp\apache\logs

    (to down the site)
        Close/Disconnect Tor Browser

        and,
        XAMPP Control Panel (click stop on apache):
            Module: Apache
            Action: Stop
