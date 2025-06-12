import { useEffect, useState } from 'react';
import axios from 'axios';

type Menu = {
  recipe_id: number;
  name: string;
  price: number;
  is_available: boolean;
};

type MenuListProps = {
  staffId?: number
  onBack: () => void;
};

const MenuList = ({ staffId, onBack }: MenuListProps) => {
  const [menuList, setMenuList] = useState<Menu[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchMenu = () => {
    setLoading(true);
    axios.get('http://localhost:8000/menu/')
      .then((res) => {
        setMenuList(res.data);
      })
      .catch((err) => {
        console.error('Error fetching menu:', err);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchMenu();
  }, []);

  if (loading) return <p>Loading menu...</p>;

  return (
    <div>
      <h1>Menu Directory</h1>
      <p style={{ textAlign: 'left' }} onClick={onBack}><button>← Back to Staff</button></p>
      <table border={1} cellPadding={8}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Available</th>
          </tr>
        </thead>
        <tbody>
          {menuList.map((menu) => (
            <tr
                key={menu.recipe_id}
                style={{
                  backgroundColor: menu.is_available ? 'white' : '#f0f0f0',
                  color: menu.is_available ? 'black' : '#888',
                  cursor: menu.is_available ? 'pointer' : 'not-allowed'
                }}
            >
              <td>{menu.name}</td>
              <td>{menu.price}</td>
              <td>{menu.is_available ? 'YES' : 'NO'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MenuList;
