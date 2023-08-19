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
              <td>
                <div>
                  <p>{item.starttime[0]}</p>
                  <p>{item.starttime[1]}</p>
                </div>
              </td>
              <td>
                <div>
                  <p>{item.endtime[0]}</p>
                  <p>{item.endtime[1]}</p>
                </div>
              </td>
              <td>
                <div>
                  <p>{item.days[0]}</p>
                  <p>{item.days[1]}</p>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Table;
