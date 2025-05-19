import { useEffect, useState } from 'react';
import axios from 'axios';

type Staff = {
  staff_id: number;
  name: string;
  date_of_birth: string;
  location: number;
};

function calculateAge(dob: string): number {
  const ageDiff = Date.now() - new Date(dob).getTime();
  const age = new Date(ageDiff).getUTCFullYear() - 1970;

  return age;
}

const StaffList = () => {
  const [staffList, setStaffList] = useState<Staff[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/staff/')
      .then((res) => {
        setStaffList(res.data);
      })
      .catch((err) => {
        console.error('Error fetching staff:', err);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading staff...</p>;

  return (
    <div>
      <h1>Staff Directory</h1>
      <table border={1} cellPadding={8}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Location ID</th>
          </tr>
        </thead>
        <tbody>
          {staffList.map((staff) => (
            <tr key={staff.staff_id}>
              <td>{staff.name}</td>
              <td>{calculateAge(staff.date_of_birth)}</td>
              <td>{staff.location}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StaffList;
