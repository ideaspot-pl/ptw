<?php

class Student
{
    public function __construct(
        public string $firstName,
        public string $lastName,
    )
    {
    }

    public function getFirstName(): string
    {
        return $this->firstName;
    }

    public function getLastName(): string
    {
        return $this->lastName;
    }

    public function getName(): string
    {
        return "{$this->getFirstName()} {$this->getLastName()}";
    }
}

$alice = new Student("Alice", "Smith");
var_dump($alice->getName());
// string 'Alice Smith' (length=11)
