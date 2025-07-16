BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS alcohol (
    mood        TEXT    NOT NULL,
    name        TEXT    NOT NULL PRIMARY KEY,
    description TEXT,
    pairing     TEXT
);

INSERT INTO alcohol (mood, name, description, pairing) VALUES
('happy',    'Champagne',  '活泼的气泡酒，柑橘与烤面包风味',       '庆祝场合'),
('tired',    'Hot Toddy',  '温暖的热托迪，蜂蜜与柠檬',            '夜晚放松'),
('nostalgic','Pinot Noir', '轻盈顺滑，草莓与樱桃香气',           '回忆时光'),
('romantic', 'Rosé',       '优雅的粉红色，草莓与花香',           '烛光晚餐'),
('stressed', 'Port Wine',  '甜美的波特酒，红色水果与巧克力香',    '散心放松');

COMMIT;
