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

INSERT OR REPLACE INTO alcohol (mood, name, description, pairing) VALUES
('excited',    'Mojito',      '清新薄荷与青柠；微甜微酸，激发活力',   '聚会派对'),
('relaxed',    'Whiskey Sour','醇厚的威士忌与柠檬酸甜碰撞，平衡放松', '下班小酌'),
('angry',      'Negroni',     '烈性琴酒+金巴利+甜苦艾酒，强烈冲击',  '情绪宣泄'),
('sad',        'Porto Tonic', '波特酒与奎宁水的意外碰撞，微微苦涩',  '夜深独酌'),
('bored',      'Gin & Tonic','简约琴酒与汤力水，清爽解闷',           '休闲时光'),
('anxious',    'Chamomile Tea Cocktail', '洋甘菊茶基底，蜂蜜调和，温柔安抚',   '静心阅读'),
('celebratory','Champagne Royale','香槟加少许利口酒，点睛华彩',         '盛大庆典');

INSERT INTO alcohol (mood, name, description, pairing) 
VALUES ('happy', '阳光鸡尾酒', '明亮清爽的柑橘口感，带有轻微的甜味', '适合搭配小食和开胃菜');
COMMIT;
