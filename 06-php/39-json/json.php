<?php

class User
{
    public string $firstName;
    public string $lastName;
    
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
}

$user = new User();
$user->setFirstName('Jon')->setLastName('Snow');

$json = json_encode($user);
$user2 = json_decode($json);

var_dump($user);
var_dump($json);
var_dump($user2);
