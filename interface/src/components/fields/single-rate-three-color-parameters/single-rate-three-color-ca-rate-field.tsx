import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorCaRateField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorCaRate = useMemo(() => {
    return singleRateThreeColorParameters.ca_rate || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorCaRate = useSetNfvTeFunctionParameter('ca_rate', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorCaRateChangeHandler = useChangeHandler(setSingleRateThreeColorCaRate);

  return (
    <FormInput
      label="Taxa de Reposição do Color Aware"
      name="ca-rate"
      value={singleRateThreeColorCaRate}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onSingleRateThreeColorCaRateChangeHandler}
    />
  );
}
