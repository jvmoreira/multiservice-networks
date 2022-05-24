import React, { ReactElement, useCallback, useMemo, useState } from 'react';

export function Display({ value }: { value: string }): ReactElement {
  const valueBlob = useMemo(() => new Blob([value], { type: 'text/plain' }), [value]);

  return (
    <section id="display-section">
      <h3>Arquivo de Configuração</h3>

      <pre>
        {value}

        <span id="action-icons">
          <CopyButton valueBlob={valueBlob} />
          <DownloadButton valueBlob={valueBlob} />
        </span>
      </pre>
    </section>
  );
}

function CopyButton({ valueBlob }: { valueBlob: Blob }): ReactElement {
  const [fillColor, setFillColor] = useState('currentColor');
  const showCopyFeedback = useCallback(() => {
    setFillColor('#6fc56a');
    setTimeout(setFillColor, 1500, 'currentColor');
  }, [setFillColor]);

  const copyHandler = useCallback(() => {
    const item = new ClipboardItem({ [valueBlob.type]: valueBlob });
    (async (): Promise<void> => {
      await navigator.clipboard.write([item]);
      showCopyFeedback();
    })();
  }, [showCopyFeedback, valueBlob]);

  return (
    <svg viewBox="0 0 24 24" onClick={copyHandler}>
      <path fill={fillColor} d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" />
    </svg>
  );
}

function DownloadButton({ valueBlob }: { valueBlob: Blob }): ReactElement {
  const anchorElement = useMemo(() => {
    const element = document.createElement('a');
    element.download = 'framework.config.json';
    return element;
  }, []);

  const downloadHandler = useCallback(() => {
    const valueObjectUrl = URL.createObjectURL(valueBlob);
    anchorElement.href = valueObjectUrl;
    document.body.appendChild(anchorElement);
    anchorElement.dispatchEvent(new MouseEvent('click'));
    document.body.removeChild(anchorElement);
    URL.revokeObjectURL(valueObjectUrl);
  }, [anchorElement, valueBlob]);

  return (
    <svg viewBox="0 0 24 24" onClick={downloadHandler}>
      <path fill="currentColor" d="M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z" />
    </svg>
  );
}
