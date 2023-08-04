import React, {useState} from "react";
import styles from '../assets/styles/form.module.css'
import {COLLEGE_OPTIONS, MAX_CLASSES} from '../utils/__constants__'

function Form(){
  const [formData, setFormData] = useState([
    { college: '', dept: '', course: '' }, 
  ]);

  // Handle changes to input fields
  const handleChange = (index, field, value) => {
    setFormData((prevFormData) => {
      const newData = [...prevFormData];
      newData[index][field] = value;
      return newData;
    });
  };

  // Handle adding new set of fields
  const handleAddFields = () => {
      setFormData((prevFormData) => [...prevFormData, { college: '', dept: '', course: '' }]);
  };

  // Handle removing a set of fields
  const handleRemoveFields = (index) => {
    setFormData((prevFormData) => {
      const newData = [...prevFormData];
      newData.splice(index, 1);
      return newData;
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Do something with formData (e.g., save it to a state)
    console.log(formData);
  };

  //React automatically gives each data array and its index in these funcs
  const classes_input = formData.map((data,index) => {
    return(
      <div key={index}>
        <select
          value={data.college}
          onChange={(e) => handleChange(index, 'college', e.target.value)}
          placeholder="College"
        >
          <option value="">Select...</option>
          {COLLEGE_OPTIONS.map((college) => {
            return(
              <option key={college} value={college}>
              {college}
              </option>
            );
          })}
        </select>
        <input
          type="text"
          value={data.dept}
          onChange={(e) => handleChange(index, 'dept', e.target.value)}
          placeholder="Dept"
        />
        <input
          type="text"
          value={data.course}
          onChange={(e) => handleChange(index, 'course', e.target.value)}
          placeholder="Course"
        />
        <button type="button" disabled={formData.length===1} onClick={() => handleRemoveFields(index)}>
          Delete
        </button>
      </div>
    );
  });

  return (
    <div className={styles.form}>
      <form onSubmit={handleSubmit}>
        <button type="add_class" onClick={handleAddFields} disabled={formData.length>=MAX_CLASSES}>
          Add Class
        </button>
        {classes_input}
        <button type="submit" disabled={formData.length<=0}>Submit</button>
      </form>
    </div>
  );
};

export default Form;
