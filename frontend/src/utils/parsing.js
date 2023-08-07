export function getCoursesInputedAsArray(formInput){
    return formInput.map(item => `${item.college}${item.dept}${item.course}`);//uses template literals
}