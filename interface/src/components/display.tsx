import React, { ReactElement } from 'react';

export function Display({ value }: { value: string }): ReactElement {
  return (
    <section id="display-section">
      <h3>Arquivo de Configuração</h3>

      <pre>{value}</pre>
    </section>
  );
}
