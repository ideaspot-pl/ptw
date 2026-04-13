<?php

ini_set('display_errors', true);

class Person
{
    private int $age;
    protected int $minAge = 18;
    
    public function getAge(): int
    {
        return $this->age;
    }
    
    public function setAge(int $age): static
    {
        $this->age = $age;
        
        return $this;
    }

}

class Student extends Person
{
    public function isAboveMinAge(): bool
    {
        return $this->getAge() >= $this->minAge;
    }
}

$student = new Student();
$student->setAge(21);
var_dump($student->getAge());
// int 21

//var_dump($student->age);
//// notice, null

var_dump($student->isAboveMinAge());
// boolean true

//var_dump($student->minAge);
//// fatal error
