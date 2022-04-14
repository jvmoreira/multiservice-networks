import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorRateField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorRate = useMemo(() => {
    return singleRateThreeColorParameters.rate || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorRate = useSetNfvTeFunctionParameter('rate', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorRateChangeHandler = useChangeHandler(setSingleRateThreeColorRate);

  return (
    <FormInput
      label="Taxa de Reposição"
      name="rate"
      value={singleRateThreeColorRate}
      placeholder="Valor de tokens adicionados a cada intervalo"
      onChange={onSingleRateThreeColorRateChangeHandler}
    />
  );
}
