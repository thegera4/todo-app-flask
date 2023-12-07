instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',  # disable foreign key constraint
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=1;',  # enable foreign key constraint
    """
        CREATE TABLE user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(200) NOT NULL
        );
    """,
    """
        CREATE TABLE todo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)
        );
    """
]
