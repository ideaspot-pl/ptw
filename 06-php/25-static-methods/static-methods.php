<?php

class Person
{
    private string $firstName;
    private string $lastName;
    
    public function getFirstName(): string
    {
        return $this->firstName;
    }
    
    public function setFirstName(string $firstName): static
    {
        $this->firstName = $firstName;
        
        return $this;
    }
    
    public function getLastName(): string
    {
        return $this->lastName;
    }
    
    public function setLastName(string $lastName): static
    {
        $this->lastName = $lastName;
        
        return $this;
    }

    public static function getType(): string
    {
        return "Person";
    }

    public static function newWithName(string $firstName, string $lastName)
    {
        $person = new self();
//        $person = new static();
        
        $person->setFirstName($firstName);
        $person->setLastName($lastName);
        
        return $person;
    }
}

class Student extends Person
{
    public static function getType(): string
    {
        return "Student";
    }
}

$person = Person::newWithName('Arya', 'Stark');
$student = Student::newWithName('Samwell', 'Tarly');

var_dump($person);
var_dump($student);
