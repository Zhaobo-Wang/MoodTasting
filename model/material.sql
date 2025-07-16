BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS material (
    alcohol_name TEXT    NOT NULL,
    ingredient   TEXT    NOT NULL,
    volume_ml    INTEGER NOT NULL,
    FOREIGN KEY(alcohol_name) REFERENCES alcohol(name)
);

INSERT INTO material (alcohol_name, ingredient, volume_ml) VALUES
('Champagne',  'Sparkling Wine Base', 120),
('Champagne',  'Orange Juice',        30),
('Hot Toddy',  'Whiskey',             50),
('Hot Toddy',  'Honey Syrup',         20),
('Hot Toddy',  'Lemon Juice',         15),
('Pinot Noir', 'Pinot Noir Wine',    100),
('Pinot Noir', 'Brandy',             20),
('Rosé',       'Rosé Wine',          120),
('Rosé',       'Strawberry Puree',    30),
('Port Wine',  'Port Wine',          100),
('Port Wine',  'Chocolate Syrup',     20);

COMMIT;
