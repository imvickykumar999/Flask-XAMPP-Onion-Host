># `Host Onion Websites` : [`index.html`](https://github.com/imvickykumar999/haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/blob/0b08ed7e1d233ca626348fbf49da90c5767c921c/index.html#L1)
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

    torrc (paste 3 lines): 
    C:\Users\Vicky\Tor Browser\Browser\TorBrowser\Data\Tor\

        HiddenServiceDir C:\Users\Vicky\Tor Browser\haystak
        HiddenServicePort 80 haystak.localhost

        HiddenServiceDir C:\Users\Vicky\Tor Browser\hackers
        HiddenServicePort 80 hackers.localhost

    index.html (add html files here): 
        C:\xampp\htdocs

    Hosted Multiple .onion links
        https://stackoverflow.com/a/42810629/11493297

    httpd-vhosts.conf
        C:\xampp\apache\conf\extra

            ServerName hackers.localhost
            DocumentRoot "C:\xampp\htdocs\hackers"

    hosts
        C:\Windows\System32\drivers\etc

            127.0.0.1  haystak.localhost
            127.0.0.1  hackers.localhost

    localhost (test locally):
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
        bkiwy4lhsoyvbxmnhee6eyv7mjz5v4ptzoyp7iejqicqh73rhf7lvead.onion

    access.log (see realtime logs): 
        C:\xampp\apache\logs

    (optional, to down the site)
        Close/Disconnect Tor Browser

        and,
        XAMPP Control Panel (click stop on apache):
            Module: Apache
            Action: Stop
