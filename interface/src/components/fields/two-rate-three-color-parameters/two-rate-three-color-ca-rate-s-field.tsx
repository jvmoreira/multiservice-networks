import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorCaRateSField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorCaRateS = useMemo(() => {
    return twoRateThreeColorParameters.ca_rateS || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorCaRateS = useSetNfvTeFunctionParameter('ca_rateS', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorCaRateSChangeHandler = useChangeHandler(setTwoRateThreeColorCaRateS);

  return (
    <FormInput
      label="Taxa de Reposição do Bucket P do Color Aware"
      name="ca-rate-s"
      value={twoRateThreeColorCaRateS}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onTwoRateThreeColorCaRateSChangeHandler}
    />
  );
}
