-- Trigger Definition in 4-store.sql
DELIMITER //

CREATE TRIGGER IF NOT EXISTS decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;
