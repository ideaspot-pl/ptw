<?php

abstract class Mobile
{
    abstract public function getNumberOfWheels(): int;
}

class Bike extends Mobile
{
    public function getNumberOfWheels(): int
    {
        return 2;
    }
}

abstract class Automobile extends Mobile
{
    abstract public function getNumberOfAxles(): int;
}

class Car extends Automobile
{
    public function getNumberOfAxles(): int
    {
        return 2;
    }

    public function getNumberOfWheels(): int
    {
        return 2 * $this->getNumberOfAxles();
    }
}

$car = new Car();
var_dump($car->getNumberOfWheels());
// int 4

$bike = new Bike();
var_dump($bike->getNumberOfWheels());
// int 2

//$autoMobile = new Automobile();
//// fatal error
