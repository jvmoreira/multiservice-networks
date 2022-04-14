import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorRateFField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorRateF = useMemo(() => {
    return twoRateThreeColorParameters.rateF || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorRateF = useSetNfvTeFunctionParameter('rateF', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorRateFChangeHandler = useChangeHandler(setTwoRateThreeColorRateF);

  return (
    <FormInput
      label="Taxa de Reposição do Bucket C"
      name="rate-f"
      value={twoRateThreeColorRateF}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onTwoRateThreeColorRateFChangeHandler}
    />
  );
}
