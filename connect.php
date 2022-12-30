<?php

$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$id = $_POST['id'];
$cell_number = $_POST['cell_number'];
$password = $_POST['password'];

//Database Conection

//Creating new Database

$connection = new mysqli('localhost', 'phpmyadmin', 'Dl5HEMzILNyF', 'register'); 
if($connection->connect_error) {                                                                                     //if connection with database dies
    die('Connection Failed : ' . $connection->connect_error);
} else {
    $sql = 'insert into Registration(first_name, last_name, id, cell_number, password) values(?, ?, ?, ?, ?)';       //sql statement
    $stmt = $connection->prepare($sql);                                                                              //prepare sql statement
    $stmt->bind_param('ssiis', $first_name, $last_name, $id, $cell_number, $password);                               //bind the the data with proper data type
    $stmt->execute();
    echo 'Registration Successful';
    $stmt->close();
    $connection->close();
}
?>