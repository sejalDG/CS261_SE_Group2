<!-- if(isset($_POST['search'])) {
  $query = "SELECT * FROM group2"
  $search_result = filterTable($query);
}
else{
  $query = "SELECT * FROM group2"
  $search_result = filterTable($query);
}


function filterTable($query)
 {
  $connect = mysqli_connect($serverName, $username, $password, $dbName);
  $filterDB = mysqli_query($connect, $query);
  return $filterDB;
} -->

<!DOCTYPE html>
<html lang="en">
<!-- Metadata for file -->
<head>
  <title>Derivative Trade Data </title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://kit.fontawesome.com/7835308eaf.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="header">
  <h1>Derivative Trade Data</h1>
</div>

<div class="sidenav">
    <title>Menu</title>
    <a href="dailytrades.html">Trade Data</a>
    <a href="addtradepage.html">Add Trade</a>
    <a href="edittrades.html">Edit Trade</a>
    <a href="deletetrades.html">Delete Trade</a>
    <a href="settingspage.html">Settings</a>
  </div>

<div class="main">
  <form>
    <label for"searchDate">Select a date:</label>
    <input type="date" id="searchDate" name="searchDate">
    <label for="sortBy">Sort By:</label>
    <select id="sortBy" name="sortBy">
      <option value="option1">Most Recent First</option>
      <option value="option2">Trade ID</option>
    </select><br>
    <label for="filterBy">Filter By:</label>
    <input type="checkbox" id="filterop1" name="filterop1"><label for="filterop1">Option 1</label>
    <input type="checkbox" id="filterop2" name="filterop2"><label for="filterop1">Option 2</label>
    <input type="submit" name="search" value="Update Results"><br><br>

    <?php
    $serverName = "group7.cz9bnfubqjbd.eu-west-2.rds.amazonaws.com";
    $username = "group7root";
    $password = "group7password";
    $dbName = "group2";

    $conn = mysqli_connect($serverName, $username, $password, $dbName);

    if (!$conn) {
      die("Connection failed: " . msqli_connect_error());
    }

    $sql = "SELECT * FROM trades_trade";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
      while($row = mysqli_fetch_assoc($result)) {
        echo "id: " . $row["id"];
      }
    } else {
      echo "0 results";
    }
    mysqli_close($conn);
    ?>
    <!--<table>
      <tr>
        <th>Trade ID</th>
        <th>Date Of Trade</th>
        <th>Time Of Trade</th>
        <th>Product</th>
        <th>Buying Party</th>
        <th>Selling Party</th>
        <th>Notional Amount</th>
        <th>Quantity</th>
        <th>Maturity Date</th>
        <th>Underlying Amount</th>
        <th>Underlying Currency</th>
        <th>Strike Price</th>
      </tr>
      <?php while($row = mysqli_fetch_array($search_result)):?>
      <tr>
        <td><?php echo $row['id'];?></td>
        <td><?php echo $row['dateCreated'];?></td>
        <td><?php echo $row['timeCreated'];?></td>
        <td><?php echo $row['prodInfo'];?></td>
        <td><?php echo $row['buyingPartyInfo'];?></td>
        <td><?php echo $row['sellingPartyInfo'];?></td>
        <td><?php echo $row['notionalAmount'];?></td>
        <td><?php echo $row['quanity'];?></td>
        <td><?php echo $row['maturityDate'];?></td>
        <td><?php echo $row['underlyingAmount'];?></td>
        <td><?php echo $row['underlyingCurrency'];?></td>
        <td><?php echo $row['strikePrice'];?></td>
      </tr>
      <?php endwhile;?>
    </table>-->
  </form>
</div>

<div class="footer">
  <h2>Footer</h2>
</div>


</body>
</html>
