import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorCaRateFField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorCaRateF = useMemo(() => {
    return twoRateThreeColorParameters.ca_rateF || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorCaRateF = useSetNfvTeFunctionParameter('ca_rateF', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorCaRateFChangeHandler = useChangeHandler(setTwoRateThreeColorCaRateF);

  return (
    <FormInput
      label="Taxa de Reposição do Bucket C do Color Aware"
      name="ca-rate-f"
      value={twoRateThreeColorCaRateF}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onTwoRateThreeColorCaRateFChangeHandler}
    />
  );
}
