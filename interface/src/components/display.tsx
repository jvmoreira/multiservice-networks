import React, { ReactElement } from 'react';

export function Display({ value }: { value: string }): ReactElement {
  return (
    <section id="display-section">
      <pre>{value}</pre>
    </section>
  );
}
