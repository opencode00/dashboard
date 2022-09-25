async function get(){
    content = await fetch("https://yelmocines.es/now-playing.aspx/GetNowPlaying", {
        "credentials": "include",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "x-datadog-origin": "rum",
            "x-datadog-parent-id": "4460279572605025572",
            "x-datadog-sampling-priority": "1",
            "x-datadog-trace-id": "539271998222162315",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        },
        "referrer": "https://yelmocines.es/cartelera/santa-cruz-tenerife",
        "body": "{'cityKey': 'santa-cruz-tenerife'}",
        "method": "POST",
        "mode": "cors"
    });
    print(content)
}
get()