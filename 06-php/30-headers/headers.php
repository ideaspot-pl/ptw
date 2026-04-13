<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PHP Headers</title>

    <style>
        main {
            display: flex;
            flex-direction: column;
            gap: 2em;
            max-width: 600px;
            margin: 0 auto;
        }

        form {
            display: inline-grid;
            grid-template-columns: 1fr 2fr;
            gap: 1em;
        }

        pre {
            background-color: #efefef;
            padding: 1ex;
            border: 1px solid silver;
        }
    </style>
</head>
<body>
<main>
    <?php if (!empty($_REQUEST)): ?>
<pre>
<?= json_encode($_REQUEST, JSON_PRETTY_PRINT); ?>
</pre>
    <?php endif; ?>
    <form method="get">
        <label for="getField">GET</label>
        <input id="getField" name="getField" type="text">
        <input type="submit" value="Send!">
    </form>
    <form method="post">
        <label for="postField">POST1</label>
        <input id="postField" name="postField" type="text">
        <label for="otherPostField">POST2</label>
        <input id="otherPostField" name="otherPostField" type="text">
        <input type="submit" value="Send!">
    </form>
</main>
</body>
</html>
