<?php

class Order
{
    const STATUS_NEW = 1;
    const STATUS_PROCESSING = 2;
    const STATUS_COMPLETE = 3;

    public int $status;

    public function getStatus(): int
    {
        return $this->status;
    }
    
    public function getStatusString(): string
    {
        return match ($this->getStatus()) {
            self::STATUS_NEW => "New",
            self::STATUS_PROCESSING => "Processing",
            self::STATUS_COMPLETE => "Complete",
            default => "Invalid",
        };
    }

    public function setStatus(int $status): static
    {
        $this->status = $status;
        
        return $this;
    }
}

$order = new Order();

$order->setStatus(Order::STATUS_NEW);
var_dump($order->getStatusString());
// string 'New' (length=3)


$order->setStatus(Order::STATUS_COMPLETE);
var_dump($order->getStatusString());
// string 'Complete' (length=8)
