<html>
  <head>
    <title>My shop</title>
  </head>

  <body>
    <h1>Welcome</h1>
    <p>List of products:</p>
    <ul>
      <?php
        // Domain name is from docker internal network
        $json = file_get_contents('http://product-service');
        $obj = json_decode($json);
        //print_r($obj);

        $products = $obj->products;
        foreach ($products as $product) {
          echo("<li>$product</li>");
        }
      ?>
    </ul>
  </body>
</html>
