<!DOCTYPE html>
<html>
<head>
    <title>API Example</title>
</head>
<body>
    <h1>API Example</h1>
    <div id="data"></div>
    <script>
        // Fetch data from the API
        fetch('https://192.168.153.203/last')
            .then(response => response.json())
            .then(data => {

//__________________________________________________________________________________

                // Prend les données de l'API

                let output = '';
                data.forEach(item => {
                    output += `<p>${item.name}: ${item.value}</p>`;
                });

//__________________________________________________________________________________

                // Affichage

                document.getElementById('data').innerHTML = output;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    </script>
</body>
</html>

