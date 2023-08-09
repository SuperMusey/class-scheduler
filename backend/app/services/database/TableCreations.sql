DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS professors;
DROP TABLE IF EXISTS course_info;
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
);

CREATE TABLE professors (
    professor_id INTEGER PRIMARY KEY,
    professor_name TEXT,
    rating REAL
);

CREATE TABLE course_info (
    class_uniqueness_id INTEGER,
    course_id INTEGER,
    professor_id INTEGER,
    start_time TEXT,
    end_time TEXT,
    days TEXT,
    PRIMARY KEY (class_uniqueness_id, course_id, professor_id, start_time, end_time, days),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
);
