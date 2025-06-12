import './App.css'
import StaffList from './pages/StaffList';
import MenuList from './pages/MenuList';
import { useState } from 'react';

function App() {
  const [selectedStaff, setSelectedStaff] = useState<number | null>(null);

  return (
    <div style={{ padding: '2rem' }}>
      {selectedStaff === null ? (
        <StaffList onSelectStaff={(staffId: number) => setSelectedStaff(staffId)} />
      ) : (
        <MenuList staffId={selectedStaff} onBack={() => setSelectedStaff(null)} />
      )}
    </div>
  )
}

export default App
