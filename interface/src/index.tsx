import React, { ReactElement } from 'react';
import { createRoot } from 'react-dom/client';
import { FormController } from '@/components/form-controller';
import './style.scss';

function App(): ReactElement {
  return <FormController />;
}

const container = document.getElementById('root');
const root = createRoot(container!);
root.render(<App />);
