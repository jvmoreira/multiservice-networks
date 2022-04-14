import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorCaBucketSMaxSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorCaBucketSMaxSize = useMemo(() => {
    return twoRateThreeColorParameters.ca_bucketS_max_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorCaBucketSMaxSize = useSetNfvTeFunctionParameter('ca_bucketS_max_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorCaBucketSMaxSizeChangeHandler = useChangeHandler(setTwoRateThreeColorCaBucketSMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket P do Color Aware"
      name="ca-bucket-s-max-size"
      value={twoRateThreeColorCaBucketSMaxSize}
      placeholder="Valor em tokens"
      onChange={onTwoRateThreeColorCaBucketSMaxSizeChangeHandler}
    />
  );
}
