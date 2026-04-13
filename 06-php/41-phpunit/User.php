<?php

class User
{
    private $firstName;
    private $lastName;
    
    public function getFirstName()
    {
        return $this->firstName;
    }
    
    public function setFirstName($firstName)
    {
        $this->firstName = $firstName;
        return $this;
    }
    
    public function getLastName()
    {
        return $this->lastName;
    }
    
    public function setLastName($lastName)
    {
        $this->lastName = $lastName;
        return $this;
    }
    
    public function getName()
    {
        return $this->firstName . ' ' . $this->lastName;
    }
    
//    public function getName()
//    {
//        if ($this->firstName && $this->lastName) {
//            return $this->firstName . ' ' . $this->lastName;
//        }
//        if ($this->firstName) {
//            return $this->firstName;
//        }
//        if ($this->lastName) {
//            return $this->lastName;
//        }
//    }
}
