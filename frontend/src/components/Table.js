import React from 'react';
import styles from '../assets/styles/table.module.css';

function Table({ data }) {
  return (
    <div className={styles.tableWrapper}>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Course</th>
            <th>Professor</th>
            <th>Rating</th>
            <th>Start</th>
            <th>End</th>
            <th>Days</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.course}</td>
              <td>{item.prof}</td>
              <td>{item.rating}</td>
              <td>{item.start}</td>
              <td>{item.end}</td>
              <td>{item.days}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Table;
