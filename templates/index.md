<!DOCTYPE html>
<head>
    <title>Hashtag Converter</title>
    <link rel="stylesheet" href="/static/index.css">
</head>
<body>
    <div class="center">
    <h1>Hashtags to Youtube Tags Converter</h1>
    <form action="/submit" method="post">
        <label for="txt">Enter Your Hashtags here:</label><br>
        <textarea id="txt" name="txt" rows="12" cols="70" onfocus="clearResult()"></textarea>
        <input type="submit" value="Submit"> 
    </form>
        <p>Converted Result:</p>
         <div class="result-container">
            <textarea id="result" name="result" rows="12" cols="70" >{{result}}</textarea>
            <button id="copy-btn" onclick="copyToClipboard()">
                <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> <span id="copy-status">Copy code</span>
            </button>
        </div>
    </div>

    <script>
        if ( window.history.replaceState ) {
        window.history.replaceState( null, null, window.location.href );
        }
        function copyToClipboard() {
            var copyText = document.getElementById("result");
            copyText.select();
            copyText.setSelectionRange(0, 99999); /*For mobile devices*/
            document.execCommand("copy");
            var copyStatus = document.getElementById("copy-status");
        copyStatus.textContent = "Copied!";
        setTimeout(function() {
            copyStatus.textContent = "Copy code";
        }, 5000);}
        
        
        function clearResult() {
            document.getElementById("result").value = "";
        }
    </script>
    

</body>
</html>
