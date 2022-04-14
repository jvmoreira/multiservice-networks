import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorRateSField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorRateS = useMemo(() => {
    return twoRateThreeColorParameters.rateS || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorRateS = useSetNfvTeFunctionParameter('rateS', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorRateSChangeHandler = useChangeHandler(setTwoRateThreeColorRateS);

  return (
    <FormInput
      label="Taxa de Reposição do Bucket P"
      name="rate-s"
      value={twoRateThreeColorRateS}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onTwoRateThreeColorRateSChangeHandler}
    />
  );
}
