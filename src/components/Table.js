import React from 'react';

function Table({ data }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Course</th>
          <th>Professor</th>
          <th>Rating</th>
          <th>Start Time</th>
          <th>End TIme</th>
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
  );
}

export default Table;
